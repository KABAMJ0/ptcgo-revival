from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import recoil_attack

card = PokemonCardDef(
    guid="e349b794-a94f-5448-8bee-019df6931727",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Greavard.Name",
    display_name="Greavard",
    searchable_by=["Greavard", "Basic", "Greavard"],
    subtypes=["Basic"],
    collector_number=65,
    set_code="ME1",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=971,
    abilities=[
        Attack(
            title="Stampede",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
        Attack(
            title="Take Down",
            game_text="This Pok\u00e9mon also does 10 damage to itself.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=recoil_attack(10),
        ),
    ],
)