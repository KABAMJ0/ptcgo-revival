from ptcgo.game.card_effects.attacks_common import flip_or_nothing
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_or_nothing

card = PokemonCardDef(
    guid="2f73ef2f-a068-5a66-8030-670c791b9d14",
    key="FUT20",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PikachuontheBall.Name",
    display_name="Pikachu on the Ball",
    searchable_by=["Pikachu on the Ball", "Basic", "PikachuontheBall"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="FUT20",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[
        Attack(
            title="Tail Whap",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Lightning Shot",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=flip_or_nothing(),
        ),
    ],
)