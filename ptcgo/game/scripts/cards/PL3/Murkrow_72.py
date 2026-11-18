from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d7b407e5-7ae6-5395-ac8d-77c522f27201",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Murkrow.Name",
    display_name="Murkrow",
    searchable_by=["Murkrow", "Basic", "Murkrow"],
    subtypes=["Basic"],
    collector_number=72,
    set_code="PL3",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=198,
    abilities=[
        Attack(
            title="Switcheroo",
            game_text="Move a Pok\u00e9mon Tool card attached to 1 of your opponent's Pok\u00e9mon to another of your opponent's Pok\u00e9mon (excluding Pok\u00e9mon that already has a Pok\u00e9mon Tool attached to it). (If an effect of this attack is prevented, this attack does nothing.)",
            cost={},
            effect=unimplemented,
        ),
        Attack(
            title="Flap",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)