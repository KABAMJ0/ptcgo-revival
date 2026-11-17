from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e14def6e-26dc-5cbf-a225-5508fe054ac9",
    key="HGSS3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gligar.Name",
    display_name="Gligar",
    searchable_by=["Gligar", "Basic", "Gligar"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="HGSS3",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    family_id=207,
    abilities=[
        Attack(
            title="Stun Poison",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed and Poisoned.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
    ],
)