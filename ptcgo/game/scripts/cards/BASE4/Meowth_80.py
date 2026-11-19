from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import draw_attack
from ptcgo.game.card_effects.attacks_common import flip_gate

card = PokemonCardDef(
    guid="704088f1-7b0f-5a39-ab5f-e92c40c0f689",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name",
    display_name="Meowth",
    searchable_by=["Meowth", "Basic", "Meowth"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="BASE4",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=52,
    abilities=[
        Attack(
            title="Pay Day",
            game_text="Flip a coin. If heads, draw a card.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            effect=flip_gate(then=draw_attack(1)),
        ),
    ],
)