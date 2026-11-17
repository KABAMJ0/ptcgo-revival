from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7ab746c7-bec3-527f-9dbf-5572200495d5",
    key="SWSH12PT5GG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HattereneVMAX.Name",
    display_name="Hatterene VMAX",
    searchable_by=["Hatterene VMAX", "VMAX", "HattereneVMAX"],
    subtypes=["VMAX"],
    collector_number=47,
    set_code="SWSH12PT5GG",
    rarity=Rarities.RareHoloVMAX,
    hp=320,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HattereneV.Name",
    family_id=858,
    abilities=[
        Ability(
            title="Witch's Domain",
            game_text="Once during your turn, you may move up to 2 damage counters from your Pok\u00e9mon to your opponent's Active Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="G-Max Smite",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=unimplemented,
        ),
    ],
)