from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="02333ee7-bd84-52e8-a8a9-1bffba70a58a",
    key="MCD19",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic", "Pikachu"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="MCD19",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=25,
    abilities=[
        Attack(
            title="Iron Tail",
            game_text="Flip a coin until you get tails. This attack does 20 damage for each heads.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            effect=flip_damage(per_heads=20, until_tails=True),
        ),
    ],
)