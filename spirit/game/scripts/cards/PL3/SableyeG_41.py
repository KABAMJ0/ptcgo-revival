from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="67e94845-88b1-58b8-84c3-7491dfeee153",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SableyeG.Name",
    display_name="Sableye G",
    searchable_by=["Sableye G", "Basic", "SP", "SableyeG"],
    subtypes=["Basic", "SP"],
    collector_number=41,
    set_code="PL3",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    resistance_type=PokemonTypes.COLORLESS,
    family_id=302,
    abilities=[
        Attack(
            title="Scratch",
            cost={},
            damage=10,
        ),
        Attack(
            title="Astonish",
            game_text="Choose 1 card from your opponent's hand without looking. Look at that card you chose, then have your opponent shuffle that card into his or her deck.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
    ],
)