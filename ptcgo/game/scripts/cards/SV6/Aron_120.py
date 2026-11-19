from ptcgo.game.card_effects.attacks_common import recoil_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0a07b8c8-1329-5deb-b3d2-c70295a7017b",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aron.Name",
    display_name="Aron",
    searchable_by=["Aron", "Basic", "Aron"],
    subtypes=["Basic"],
    collector_number=120,
    set_code="SV6",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=304,
    abilities=[
        Attack(
            title="Double-Edge",
            game_text="This Pok\u00e9mon also does 10 damage to itself.",
            cost={PokemonTypes.METAL: 1},
            damage=20,
            effect=recoil_attack(10),
        ),
    ],
)