from ptcgo.game.card_effects.trainers import draw_n
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from ptcgo.game.card_effects.attacks_common import bonus_if

def _same_hand_size(ctx):
    return ctx.hand_size() == ctx.hand_size(ctx.opponent_id)

card = PokemonCardDef(
    guid="5d29375b-97af-5503-8ae7-476896616c8f",
    key="SWSH10TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wyrdeer.Name",
    display_name="Wyrdeer",
    searchable_by=["Wyrdeer", "Stage 1", "Wyrdeer"],
    subtypes=["Stage 1"],
    collector_number=6,
    set_code="SWSH10TG",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Stantler.Name",
    family_id=899,
    abilities=[
        Ability(
            title="Hurried Gait",
            game_text="Once during your turn, you may draw a card.",
            effect=draw_n(1),
        ),
        Attack(
            title="Extrasensory",
            game_text="If you have the same number of cards in your hand as your opponent, this attack does 80 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=bonus_if(_same_hand_size, 80),
        ),
    ],
)