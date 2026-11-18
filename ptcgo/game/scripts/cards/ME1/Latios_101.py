from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0146dde9-7c58-5884-a304-9b5fc5a1eaf2",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latios.Name",
    display_name="Latios",
    searchable_by=["Latios", "Basic", "Latios"],
    subtypes=["Basic"],
    collector_number=101,
    set_code="ME1",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=381,
    abilities=[
        Ability(
            title="Lustrous Assist",
            game_text="Once during your turn, when your Mega Latias ex moves from your Bench to the Active Spot, you may use this Ability. Move any amount of Energy from your Benched Pok\u00e9mon to your Active Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Dragon Claw",
            cost={PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)