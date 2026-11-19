from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

card = PokemonCardDef(
    guid="041426be-688d-5c38-9ec0-7025a5e52931",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Octillery.Name",
    display_name="Octillery",
    searchable_by=["Octillery", "Stage 1", "Octillery"],
    subtypes=["Stage 1"],
    collector_number=17,
    set_code="ME4",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Remoraid.Name",
    family_id=223,
    abilities=[
        Attack(
            title="Jet of Ink",
            game_text="During your opponent's next turn, if the Defending Pok\u00e9mon tries to use an attack, your opponent flips 2 coins. If either of them is tails, that attack doesn't happen.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Tantrum",
            game_text="This Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=condition_attack(SpecialConditions.CONFUSED, self_conditions=(SpecialConditions.CONFUSED,)),
        ),
    ],
)