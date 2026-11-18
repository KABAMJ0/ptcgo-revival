from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c4bd9366-b4d4-5a31-b53f-287bac195dfd",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Delphox.Name",
    display_name="Delphox",
    searchable_by=["Delphox", "Stage 2", "Delphox"],
    subtypes=["Stage 2"],
    collector_number=26,
    set_code="XY1",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Braixen.Name",
    family_id=653,
    abilities=[
        Ability(
            title="Mystical Fire",
            game_text="Once during your turn (before your attack), you may draw cards until you have 6 cards in your hand.",
            effect=unimplemented,
        ),
        Attack(
            title="Blaze Ball",
            game_text="This attack does 20 more damage for each Fire Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)