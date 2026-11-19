from ptcgo.game.card_effects.attacks_common import recoil_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="519fd25a-8b28-5552-846b-23f916fbef42",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beldum.Name",
    display_name="Beldum",
    searchable_by=["Beldum", "Basic", "Beldum"],
    subtypes=["Basic"],
    collector_number=113,
    set_code="SV5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=374,
    abilities=[
        Attack(
            title="Dig Claws",
            cost={PokemonTypes.METAL: 1},
            damage=10,
        ),
        Attack(
            title="Iron Tackle",
            game_text="This Pok\u00e9mon also does 10 damage to itself.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=recoil_attack(10),
        ),
    ],
)