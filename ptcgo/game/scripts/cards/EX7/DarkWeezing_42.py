from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="84daf00c-e741-589e-bd32-6ceeac3bfafb",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkWeezing.Name",
    display_name="Dark Weezing",
    searchable_by=["Dark Weezing", "Stage 1", "DarkWeezing"],
    subtypes=["Stage 1"],
    collector_number=42,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS, PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name",
    family_id=109,
    abilities=[
        Ability(
            title="Methane Leak",
            game_text="As long as Dark Weezing is your Active Pok\u00e9mon, put 1 damage counter on each Pok\u00e9mon that remains Poisoned between turns.",
            effect=unimplemented,
        ),
        Attack(
            title="Smog",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.POISONED),
        ),
        Attack(
            title="Darkness Charge",
            game_text="Put 2 damage counters on Dark Weezing.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=unimplemented,
        ),
    ],
)