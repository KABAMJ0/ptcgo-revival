from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="44639432-dfd6-58ff-ac09-b86a8951ef0d",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Annihilape.Name",
    display_name="Annihilape",
    searchable_by=["Annihilape", "Stage 2", "Annihilape"],
    subtypes=["Stage 2"],
    collector_number=47,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Primeape.Name",
    family_id=56,
    abilities=[
        Attack(
            title="Rage Fist",
            game_text="This attack does 70 damage for each Prize card your opponent has taken.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=70,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Dynamite Punch",
            game_text="This Pok\u00e9mon also does 50 damage to itself.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=170,
            effect=unimplemented,
        ),
    ],
)