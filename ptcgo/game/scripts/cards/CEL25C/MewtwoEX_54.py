from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2c036036-b5b1-56c9-b0d9-3729462ca18b",
    key="CEL25C",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MewtwoEX.Name",
    display_name="Mewtwo-EX",
    searchable_by=["Mewtwo-EX", "Basic", "EX", "MewtwoEX"],
    subtypes=["Basic", "EX"],
    collector_number=54,
    set_code="CEL25C",
    rarity=Rarities.Common,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=150,
    abilities=[
        Attack(
            title="X Ball",
            game_text="Does 20 damage times the amount of Energy attached to this Pok\u00e9mon and the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Psydrive",
            game_text="Discard an Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)