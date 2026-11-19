from ptcgo.game.card_effects.attacks_common import flip_or_nothing
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ad2adc6b-9607-5b43-b221-2db7a0c3faae",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HeracrossE4.Name",
    display_name="Heracross E4",
    searchable_by=["Heracross E4", "Basic", "SP", "HeracrossE4"],
    subtypes=["Basic", "SP"],
    collector_number=24,
    set_code="PL2",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=214,
    abilities=[
        Attack(
            title="Focus Energy",
            game_text="During your next turn, Heracross E4's Megahorn attack's base damage is 100.",
            cost={},
            effect=unimplemented,
        ),
        Attack(
            title="Megahorn",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=flip_or_nothing(),
        ),
    ],
)