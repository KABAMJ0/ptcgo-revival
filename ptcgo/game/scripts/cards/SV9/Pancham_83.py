from ptcgo.game.card_effects.attacks_common import flip_or_nothing
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="13d1815f-6636-5c34-82b0-4fee761c53bb",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pancham.Name",
    display_name="Pancham",
    searchable_by=["Pancham", "Basic", "Pancham"],
    subtypes=["Basic"],
    collector_number=83,
    set_code="SV9",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=674,
    abilities=[
        Attack(
            title="Corkscrew Punch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Focus Fist",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            effect=flip_or_nothing(),
        ),
    ],
)