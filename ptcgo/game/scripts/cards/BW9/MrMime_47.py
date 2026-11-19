from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.session.passives import Passive


class BenchBarrierPassive(Passive):
    """Attack damage to this player's own Benched Pokemon is prevented."""

    def blocks_bench_damage(self, calc, carrier):
        return calc.target is not None and \
            calc.target.owning_player_id == carrier.owning_player_id

card = PokemonCardDef(
    guid="7ebe9ee1-6e30-59f4-b858-4f0081b39373",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MrMime.Name",
    display_name="Mr. Mime",
    searchable_by=["Mr. Mime", "Basic", "MrMime"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="BW9",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=122,
    abilities=[
        Ability(
            title="Bench Barrier",
            game_text="Prevent all damage done to your Benched Pok\u00e9mon by attacks.",
            passive=BenchBarrierPassive(),
        ),
        Attack(
            title="Psy Bolt",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)