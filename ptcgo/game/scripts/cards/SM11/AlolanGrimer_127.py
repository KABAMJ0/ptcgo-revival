from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import draw_attack

card = PokemonCardDef(
    guid="5521fc30-86ae-53f4-9e7b-7c0467cd2df4",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGrimer.Name",
    display_name="Alolan Grimer",
    searchable_by=["Alolan Grimer", "Basic", "AlolanGrimer"],
    subtypes=["Basic"],
    collector_number=127,
    set_code="SM11",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=88,
    abilities=[
        Attack(
            title="Collect",
            game_text="Draw 2 cards.",
            cost={},
            effect=draw_attack(2),
        ),
        Attack(
            title="Sludge Bomb",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)