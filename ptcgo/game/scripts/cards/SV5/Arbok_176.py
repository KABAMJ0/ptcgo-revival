from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="cc02c67b-528b-5f9d-ab0e-ff4e4e70bd5d",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arbok.Name",
    display_name="Arbok",
    searchable_by=["Arbok", "Stage 1", "Arbok"],
    subtypes=["Stage 1"],
    collector_number=176,
    set_code="SV5",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ekans.Name",
    family_id=23,
    abilities=[
        Attack(
            title="Panic Poison",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned, Confused, and Poisoned.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=condition_attack(SpecialConditions.BURNED, SpecialConditions.CONFUSED, SpecialConditions.POISONED),
        ),
        Attack(
            title="Darkness Fang",
            cost={PokemonTypes.DARKNESS: 2},
            damage=70,
        ),
    ],
)