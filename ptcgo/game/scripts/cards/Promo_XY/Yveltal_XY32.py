from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack, flip_discard_opponent_energy, flip_gate
from ptcgo.game.card_effects.passives_common import composed
from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="a32cf30b-822f-5e28-b022-c431dc042320",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yveltal.Name",
    display_name="Yveltal",
    searchable_by=["Yveltal", "Basic", "Yveltal"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=717,
    abilities=[
        Attack(
            title="Air Crash",
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=composed(lambda ctx: ctx.deal_damage(), flip_gate(then=discard_opponent_energy_attack(1, damage=0))),
        ),
        Attack(
            title="Wings of Destruction",
            game_text="If your opponent has Xerneas (including Xerneas-EX) in play, this attack does 40 more damage.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)