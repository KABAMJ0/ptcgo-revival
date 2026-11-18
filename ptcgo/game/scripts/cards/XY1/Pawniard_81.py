from ptcgo.game.card_effects.passives_common import composed
from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack, flip_gate
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2a8a8826-9f09-53ea-beeb-3302a975edbe",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pawniard.Name",
    display_name="Pawniard",
    searchable_by=["Pawniard", "Basic", "Pawniard"],
    subtypes=["Basic"],
    collector_number=81,
    set_code="XY1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=624,
    abilities=[
        Attack(
            title="Cut Down",
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1},
            effect=composed(lambda ctx: ctx.deal_damage(), flip_gate(then=discard_opponent_energy_attack(1, damage=0))),
        ),
        Attack(
            title="Metal Claw",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)