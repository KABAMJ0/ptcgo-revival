from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c14cf226-162a-558a-9618-bca38685f0e5",
    key="HGSS1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sunflora.Name",
    display_name="Sunflora",
    searchable_by=["Sunflora", "Stage 1", "Sunflora"],
    subtypes=["Stage 1"],
    collector_number=31,
    set_code="HGSS1",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sunkern.Name",
    family_id=191,
    abilities=[
        Ability(
            title="Sunshine Grace",
            game_text="Once during your turn (before your attack), you may search your deck for a Grass Pok\u00e9mon, show it to your opponent, and put it into your hand. Shuffle your deck afterward. This power can't be used if Sunflora is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Blade Arms",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)