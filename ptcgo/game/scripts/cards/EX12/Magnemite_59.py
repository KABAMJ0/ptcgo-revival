from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9aa2958f-8d43-525a-a3f3-f255f241514c",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name",
    display_name="Magnemite",
    searchable_by=["Magnemite", "Basic", "Magnemite"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="EX12",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=81,
    abilities=[
        Attack(
            title="Magnetic Swirl",
            game_text="Flip a coin. If tails, this attack does nothing. If heads, discard an Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)