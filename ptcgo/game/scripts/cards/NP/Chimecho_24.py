from ptcgo.game.card_effects.passives_common import composed
from ptcgo.game.card_effects.support_common import heal_targets
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

card = PokemonCardDef(
    guid="330f9202-4cdc-566a-ac60-faf255fa6328",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chimecho.Name",
    display_name="Chimecho",
    searchable_by=["Chimecho", "Basic", "Chimecho"],
    subtypes=["Basic"],
    collector_number=24,
    set_code="NP",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=358,
    abilities=[
        Attack(
            title="Resonate",
            game_text="Your opponent switches each Defending Pok\u00e9mon with his or her Benched Pok\u00e9mon. If your opponent has only 1 Benched Pok\u00e9mon, you choose the Defending Pok\u00e9mon to switch.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Healing Sound",
            game_text="Remove 3 damage counters from each of your Active Pok\u00e9mon. Each Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=composed(heal_targets(30, "each_own"), condition_attack(SpecialConditions.ASLEEP, both_actives=True)),
        ),
    ],
)