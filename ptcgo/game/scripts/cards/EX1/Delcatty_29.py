from ptcgo.game.card_effects.attacks_common import damage_per_extra_energy
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="622a0ecd-7195-5de7-82d1-4deb35caaf1f",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Delcatty.Name",
    display_name="Delcatty",
    searchable_by=["Delcatty", "Stage 1", "Delcatty"],
    subtypes=["Stage 1"],
    collector_number=29,
    set_code="EX1",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skitty.Name",
    family_id=300,
    abilities=[
        Attack(
            title="Energy Call",
            game_text="Attach 1 Energy card from your discard pile to your Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Cannonball",
            game_text="Does 30 damage plus 10 more damage for each Energy attached to Delcatty but not used to pay for this attack's Energy cost.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=damage_per_extra_energy(10, base=30),
        ),
    ],
)