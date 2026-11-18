from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cd22cd11-0690-5974-a263-77ad70017a8e",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GardevoirLVX.Name",
    display_name="Gardevoir LV.X",
    searchable_by=["Gardevoir LV.X", "Level-Up", "GardevoirLVX"],
    subtypes=["Level-Up"],
    collector_number=131,
    set_code="DP3",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gardevoir.Name",
    family_id=280,
    abilities=[
        Ability(
            title="Teleportation",
            game_text="Once during your turn (before your attack), choose 1 of your Active Pok\u00e9mon or 1 or your Benched Pok\u00e9mon and switch Gardevoir with that Pok\u00e9mon. This power can't be used if Gardevoir is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Bring Down",
            game_text="Choose 1 Pok\u00e9mon (yours or your opponent's) with the fewest remaining HP (excluding Gardevoir) and that Pok\u00e9mon is now Knocked Out.",
            cost={PokemonTypes.PSYCHIC: 2},
            effect=unimplemented,
        ),
    ],
)