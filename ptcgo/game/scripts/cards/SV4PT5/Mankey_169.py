from ptcgo.game.card_effects.attacks_common import recoil_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ab88bc76-464e-5e65-b487-1ef18a932543",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mankey.Name",
    display_name="Mankey",
    searchable_by=["Mankey", "Basic", "Mankey"],
    subtypes=["Basic"],
    collector_number=169,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=56,
    abilities=[
        Attack(
            title="Monkey Beatdown",
            game_text="This Pok\u00e9mon also does 10 damage to itself.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=recoil_attack(10),
        ),
    ],
)