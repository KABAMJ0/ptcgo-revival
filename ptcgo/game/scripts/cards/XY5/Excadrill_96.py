from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack, flip_discard_opponent_energy, flip_gate
from ptcgo.game.card_effects.passives_common import composed
from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="d82d717f-45ff-56af-8d91-97ee8eea2886",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Excadrill.Name",
    display_name="Excadrill",
    searchable_by=["Excadrill", "Stage 1", "Excadrill"],
    subtypes=["Stage 1"],
    collector_number=96,
    set_code="XY5",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drilbur.Name",
    family_id=529,
    abilities=[
        Attack(
            title="Drill Run",
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1},
            damage=20,
            effect=composed(lambda ctx: ctx.deal_damage(), flip_gate(then=discard_opponent_energy_attack(1, damage=0))),
        ),
        Attack(
            title="Straight Claw",
            game_text="You may discard an Energy attached to this Pok\u00e9mon. If you do, this attack does 30 more damage.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)