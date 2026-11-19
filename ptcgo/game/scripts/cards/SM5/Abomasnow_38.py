from ptcgo.game.card_effects.trainers import basic_energy_of
from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="76d9a03d-497e-5c7b-9acf-5ffe9b39c5d2",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Abomasnow.Name",
    display_name="Abomasnow",
    searchable_by=["Abomasnow", "Stage 1", "Abomasnow"],
    subtypes=["Stage 1"],
    collector_number=38,
    set_code="SM5",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snover.Name",
    family_id=459,
    abilities=[
        Ability(
            title="Blessings of the Frost",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may attach a Water Energy card from your discard pile to 1 of your Pok\u00e9mon.",
            trigger=Triggers.ON_EVOLVE,
            effect=attach_from_discard(basic_energy_of("Water"), count=1, target="choice"),
        ),
        Attack(
            title="Hypno Hammer",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)