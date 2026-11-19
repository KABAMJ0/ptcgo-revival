from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import bonus_if
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.content.definitions import Activations

async def mend(ctx):
    attached = await attach_from_discard(
        lambda card: energy_provides_type(card, PokemonTypes.FIGHTING.value),
        count=1, target="self", minimum=0,
        prompt="Choose a Fighting Energy card from your discard pile",
    )(ctx)
    if attached and ctx.source is not None:
        await ctx.heal(10, ctx.source)

def _named_in_play(name, side="mine"):
    """Printed-name test: the corpus stores EVOLUTION_LOGIC_NAME without the
    space ("Regirockex"), so a literal `named_in_play("Regirock ex")` is false
    forever. Compare the display name instead."""
    from ptcgo.game.content.definitions import def_for

    def cond(ctx):
        pool = (ctx.my_pokemon_in_play() if side == "mine"
                else ctx.opponent_pokemon_in_play())
        for pokemon in pool:
            definition = def_for(pokemon.archetype_id)
            if definition is not None and definition.display_name == name:
                return True
        return False
    return cond


card = PokemonCardDef(
    guid="46e5601b-dc81-58f6-8881-81cf6bd73ec8",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regirockex.Name",
    display_name="Regirock ex",
    searchable_by=["Regirock ex", "Basic", "ex", "Regirockex"],
    subtypes=["Basic", "ex"],
    collector_number=99,
    set_code="EX9",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=377,
    abilities=[
        Attack(
            title="Mend",
            game_text="Search your discard pile for a Fighting Energy card and attach it to Regirock ex. If you do, remove 1 damage counter from Regirock ex.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=mend,
        ),
        Attack(
            title="Metal Crush",
            game_text="If Registeel ex is in play, this attack does 40 damage plus 20 more damage.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="+",
            effect=bonus_if(_named_in_play("Registeel ex"), 20, base=40),
        ),
    ],
)