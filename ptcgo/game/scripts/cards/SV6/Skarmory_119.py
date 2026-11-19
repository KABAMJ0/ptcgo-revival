from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import discard_stadium_attack

card = PokemonCardDef(
    guid="a329bb78-227d-52b6-b737-403fa47a5192",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skarmory.Name",
    display_name="Skarmory",
    searchable_by=["Skarmory", "Basic", "Skarmory"],
    subtypes=["Basic"],
    collector_number=119,
    set_code="SV6",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=227,
    abilities=[
        Attack(
            title="Cutting Wind",
            cost={PokemonTypes.METAL: 1},
            damage=30,
        ),
        Attack(
            title="Big Storm",
            game_text="Discard a Stadium in play.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
            effect=discard_stadium_attack(),
        ),
    ],
)