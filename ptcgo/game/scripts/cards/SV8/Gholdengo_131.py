from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import psychic_leap


card = PokemonCardDef(
    guid="e41bb8b3-04d7-5b58-982a-d55cb9c00259",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gholdengo.Name",
    display_name="Gholdengo",
    searchable_by=["Gholdengo", "Stage 1", "Gholdengo"],
    subtypes=["Stage 1"],
    collector_number=131,
    set_code="SV8",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gimmighoul.Name",
    family_id=999,
    abilities=[
        Attack(
            title="Strike It Rich",
            game_text="If this Pok\u00e9mon evolved from Gimmighoul during this turn, this attack does 90 more damage.",
            cost={PokemonTypes.METAL: 1},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Surf Back",
            game_text="You may shuffle this Pok\u00e9mon and all attached cards into your deck.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=psychic_leap,
        ),
    ],
)