from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1a65ec88-9c9d-5f38-b2d4-765bfc647c0e",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swalot.Name",
    display_name="Swalot",
    searchable_by=["Swalot", "Stage 1", "Swalot"],
    subtypes=["Stage 1"],
    collector_number=9,
    set_code="PL4",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gulpin.Name",
    family_id=316,
    abilities=[
        Attack(
            title="Damage Roller",
            game_text="Put damage counters on the Defending Pok\u00e9mon until the Defending Pok\u00e9mon has the same remaining HP as Swalot. (If the Defending Pok\u00e9mon has the same or less remaining HP as Swalot, this attack does nothing.)",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Entangle Tackle",
            game_text="You may do 50 damage plus 30 more damage. If you do, this attack does 30 damage to 1 of your Pok\u00e9mon, and don't apply Weakness and Resistance to this damage.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)