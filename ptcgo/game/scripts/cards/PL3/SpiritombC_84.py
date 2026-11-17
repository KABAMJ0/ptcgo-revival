from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="09584f7a-093a-5505-a967-a657183333a1",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SpiritombC.Name",
    display_name="Spiritomb C",
    searchable_by=["Spiritomb C", "Basic", "SP", "SpiritombC"],
    subtypes=["Basic", "SP"],
    collector_number=84,
    set_code="PL3",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    resistance_type=PokemonTypes.COLORLESS,
    family_id=442,
    abilities=[
        Attack(
            title="Sharpshooting",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 10 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Lock Up",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
    ],
)