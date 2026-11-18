from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.card_effects.support_common import look_top_attach_energy

card = PokemonCardDef(
    guid="d35dbf0e-2dd6-5560-a296-87c55fe02816",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name",
    display_name="Gloom",
    searchable_by=["Gloom", "Stage 1", "Gloom"],
    subtypes=["Stage 1"],
    collector_number=44,
    set_code="SV3PT5",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Oddish.Name",
    family_id=43,
    abilities=[
        Ability(
            title="Semi-Blooming Energy",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may look at the top 3 cards of your deck and attach any number of Basic Energy cards you find there to your Pok\u00e9mon in any way you like. Shuffle the other cards back into your deck.",
            trigger=Triggers.ON_EVOLVE,
            effect=look_top_attach_energy(3, is_basic_energy_card),
        ),
        Attack(
            title="Drool",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)