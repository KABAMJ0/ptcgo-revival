from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack, flip_discard_opponent_energy, flip_gate
from ptcgo.game.card_effects.passives_common import composed
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="61585493-b07d-54d0-9b6f-cc302bb2b88b",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Noibat.Name",
    display_name="Noibat",
    searchable_by=["Noibat", "Basic", "Noibat"],
    subtypes=["Basic"],
    collector_number=132,
    set_code="XY8",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=714,
    abilities=[
        Attack(
            title="Mysterious Beam",
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=composed(lambda ctx: ctx.deal_damage(), flip_gate(then=discard_opponent_energy_attack(1, damage=0))),
        ),
        Attack(
            title="Gust",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)