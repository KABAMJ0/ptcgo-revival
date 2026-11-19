from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import AttrID

async def aroma_of_gratitude(ctx):
    """Heal 20 from each of your Benched Basic Pokemon."""
    from ptcgo.game.attributes import PokemonStage
    for pokemon in list(ctx.my_bench()):
        if pokemon.get_attribute(AttrID.STAGE) != PokemonStage.BASIC.value:
            continue
        await ctx.heal(20, target=pokemon)


card = PokemonCardDef(
    guid="db7627e5-ae1d-538b-9867-899fae093bdb",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShayminEX.Name",
    display_name="Shaymin-EX",
    searchable_by=["Shaymin-EX", "Basic", "EX", "ShayminEX"],
    subtypes=["Basic", "EX"],
    collector_number=148,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=492,
    abilities=[
        Ability(
            title="Aroma of Gratitude",
            game_text="Once during your turn (before your attack), you may heal 20 damage from each of your Benched Basic Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            effect=aroma_of_gratitude,
        ),
        Attack(
            title="Floral Gain",
            game_text="Heal 20 damage and remove all Special Conditions from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=unimplemented,
        ),
    ],
)