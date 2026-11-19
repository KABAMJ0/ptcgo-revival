from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="5508c853-a422-55ce-8fa1-581abbd00baa",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shieldon.Name",
    display_name="Shieldon",
    searchable_by=["Shieldon", "Stage 1", "Shieldon"],
    subtypes=["Stage 1"],
    collector_number=61,
    set_code="ME5",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AntiqueArmorFossil.Name",
    family_id=410,
    abilities=[
        Attack(
            title="Smithereen Smash",
            game_text="Discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=discard_opponent_energy_attack(1),
        ),
    ],
)