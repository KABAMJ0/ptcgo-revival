from ptcgo.game.card_effects.support_common import heal_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7921756a-3718-558f-beaf-461f06720f31",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ceruledge.Name",
    display_name="Ceruledge",
    searchable_by=["Ceruledge", "Stage 1", "Ceruledge"],
    subtypes=["Stage 1"],
    collector_number=40,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charcadet.Name",
    family_id=935,
    abilities=[
        Attack(
            title="Life Sucker",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=heal_attack(30),
        ),
        Attack(
            title="Fighting Sword",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon ex or Pok\u00e9mon V, this attack does 100 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)