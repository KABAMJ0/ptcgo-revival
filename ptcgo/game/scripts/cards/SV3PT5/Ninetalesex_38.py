from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.trainers import draw_n
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from ptcgo.game.card_effects.attacks_common import bonus_if

def _same_hand_size(ctx):
    return ctx.hand_size() == ctx.hand_size(ctx.opponent_id)

card = PokemonCardDef(
    guid="21fd84d2-ba9b-51e7-9529-42d0b4539841",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ninetalesex.Name",
    display_name="Ninetales ex",
    searchable_by=["Ninetales ex", "Stage 1", "ex", "Ninetalesex"],
    subtypes=["Stage 1", "ex"],
    collector_number=38,
    set_code="SV3PT5",
    rarity=Rarities.Rare,
    hp=260,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name",
    family_id=37,
    abilities=[
        Attack(
            title="Heat Wave",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.BURNED),
        ),
        Attack(
            title="Mirrored Flames",
            game_text="If you have the same number of cards in your hand as your opponent, this attack does 140 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=bonus_if(_same_hand_size, 140),
        ),
    ],
)