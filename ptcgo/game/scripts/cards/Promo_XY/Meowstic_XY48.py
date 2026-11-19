from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack, flip_discard_opponent_energy, flip_gate
from ptcgo.game.card_effects.passives_common import composed
from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="5b98e7c0-3e5b-5ee4-9037-03153ce49821",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meowstic.Name",
    display_name="Meowstic",
    searchable_by=["Meowstic", "Stage 1", "Meowstic"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Espurr.Name",
    family_id=678,
    abilities=[
        Ability(
            title="Mysterious Ears",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if this Pok\u00e9mon is Knocked Out), the Attacking Pok\u00e9mon is now Confused.",
            effect=unimplemented,
        ),
        Attack(
            title="Psyblast",
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=composed(lambda ctx: ctx.deal_damage(), flip_gate(then=discard_opponent_energy_attack(1, damage=0))),
        ),
    ],
)