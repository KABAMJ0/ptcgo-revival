from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import recoil_attack

card = PokemonCardDef(
    guid="1f0f4aaa-69ad-5fe7-b8d9-6c7a2d728a17",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electrike.Name",
    display_name="Electrike",
    searchable_by=["Electrike", "Basic", "Electrike"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="ME1",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=309,
    abilities=[
        Attack(
            title="Thunder Jolt",
            game_text="This Pok\u00e9mon also does 10 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=recoil_attack(10),
        ),
    ],
)