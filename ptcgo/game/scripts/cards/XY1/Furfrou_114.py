from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack, flip_discard_opponent_energy, flip_gate
from ptcgo.game.card_effects.passives_common import composed
from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="a7078adb-bab0-582f-a800-a1f2536ad00a",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Furfrou.Name",
    display_name="Furfrou",
    searchable_by=["Furfrou", "Basic", "Furfrou"],
    subtypes=["Basic"],
    collector_number=114,
    set_code="XY1",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=676,
    abilities=[
        Ability(
            title="Fur Coat",
            game_text="Any damage done to this Pok\u00e9mon by attacks is reduced by 20 (after applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Energy Cutoff",
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=composed(lambda ctx: ctx.deal_damage(), flip_gate(then=discard_opponent_energy_attack(1, damage=0))),
        ),
    ],
)