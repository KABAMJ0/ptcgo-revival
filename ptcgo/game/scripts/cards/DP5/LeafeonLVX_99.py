from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6360b467-f0e9-5aba-9727-e5bb5822c7c0",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LeafeonLVX.Name",
    display_name="Leafeon LV.X",
    searchable_by=["Leafeon LV.X", "Level-Up", "LeafeonLVX"],
    subtypes=["Level-Up"],
    collector_number=99,
    set_code="DP5",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Leafeon.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Energy Forcing",
            game_text="Once during your turn (before your attack), you may attach an Energy card from your hand to 1 of your Pok\u00e9mon. This power can't be used if Leafeon is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Verdant Dance",
            game_text="Does 30 damage plus 10 more damage for each Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)