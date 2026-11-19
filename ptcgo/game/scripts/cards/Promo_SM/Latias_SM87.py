from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.session.effects import is_basic_pokemon
from ptcgo.game.card_effects.attacks_common import lock_defender_attacks
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def sugary_sprinkles(ctx):
    """Heal 30 damage from each of your Benched Pokemon."""
    for pokemon in ctx.my_bench():
        await ctx.heal(30, pokemon)

card = PokemonCardDef(
    guid="78602eea-0ffe-5207-bd42-408cff16bb51",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latias.Name",
    display_name="Latias",
    searchable_by=["Latias", "Basic", "Latias"],
    subtypes=["Basic"],
    collector_number=87,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=380,
    abilities=[
        Ability(
            title="Flight Support",
            game_text="Your Latios in play have no Retreat Cost.",
            effect=unimplemented,
        ),
        Attack(
            title="Misty Gale",
            game_text="Heal 30 damage from each of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=sugary_sprinkles,
        ),
    ],
)