from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import lock_defender_attacks
from ptcgo.game.session.effects import is_basic_pokemon


async def tie_up(ctx):
    """20. If the Defending Pokemon is a Basic Pokemon, it can't attack next turn."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None and is_basic_pokemon(defender):
        lock_defender_attacks(ctx)


card = PokemonCardDef(
    guid="3eb8b390-d51a-528e-8e01-4667ef815966",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spiritomb.Name",
    display_name="Spiritomb",
    searchable_by=["Spiritomb", "Basic", "Spiritomb"],
    subtypes=["Basic"],
    collector_number=53,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=442,
    abilities=[
        Attack(
            title="Lightless World",
            game_text="Put 2 Supporter cards from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Terrify",
            game_text="If the Defending Pok\u00e9mon is a Basic Pok\u00e9mon, it can't attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=tie_up,
        ),
    ],
)