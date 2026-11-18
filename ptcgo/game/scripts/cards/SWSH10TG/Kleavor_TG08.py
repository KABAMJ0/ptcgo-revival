from ptcgo.game.card_effects.attacks_common import recoil_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b1febf35-587d-5802-b0cf-ac11ef87a791",
    key="SWSH10TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kleavor.Name",
    display_name="Kleavor",
    searchable_by=["Kleavor", "Stage 1", "Kleavor"],
    subtypes=["Stage 1"],
    collector_number=8,
    set_code="SWSH10TG",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scyther.Name",
    family_id=900,
    abilities=[
        Attack(
            title="Timber Cleave",
            game_text="Flip 2 coins. If both of them are heads, your opponent's Active Pok\u00e9mon is Knocked Out.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Berserker Tackle",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=120,
            effect=recoil_attack(30),
        ),
    ],
)