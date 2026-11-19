from ptcgo.game.card_effects.attacks_common import reveal_hand_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="53340fb6-ff18-5be8-a514-5692fea11076",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drowzee.Name",
    display_name="Drowzee",
    searchable_by=["Drowzee", "Basic", "Drowzee"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="SV6PT5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=96,
    abilities=[
        Attack(
            title="Eerie Gaze",
            game_text="Your opponent reveals their hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=reveal_hand_attack(),
        ),
    ],
)