from ptcgo.game.card_effects.attacks_common import recoil_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9269ea9f-2555-5ea7-ac12-562bf02974d8",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Koraidonex.Name",
    display_name="Koraidon ex",
    searchable_by=["Koraidon ex", "Basic", "ex", "Ancient", "Koraidonex"],
    subtypes=["Basic", "ex", "Ancient"],
    collector_number=120,
    set_code="SV5",
    rarity=Rarities.Rare,
    hp=230,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=1007,
    abilities=[
        Attack(
            title="Retribution Strike",
            game_text="This attack does 10 more damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Kaiser Tackle",
            game_text="This Pok\u00e9mon also does 60 damage to itself.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.FIGHTING: 2},
            damage=280,
            effect=recoil_attack(60),
        ),
    ],
)