from ptcgo.game.card_effects.attacks_common import damage_all_opponents
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import named_in_play
from ptcgo.game.attributes import SpecialConditions

async def block_signal(ctx):
    if not _named_in_play("Regice ex")(ctx):
        return
    results = await ctx.flip_coins(1, "Block Signal")
    if results and results[0]:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.CONFUSED)

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
    guid="2996ccfd-0687-535b-bcfb-4ebeaa04c1d1",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Registeelex.Name",
    display_name="Registeel ex",
    searchable_by=["Registeel ex", "Basic", "ex", "Registeelex"],
    subtypes=["Basic", "ex"],
    collector_number=100,
    set_code="EX9",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=379,
    abilities=[
        Attack(
            title="Block Signal",
            game_text="If Regice ex is in play, flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=block_signal,
        ),
        Attack(
            title="Wide Laser",
            game_text="Does 20 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            effect=damage_all_opponents(20),
        ),
    ],
)