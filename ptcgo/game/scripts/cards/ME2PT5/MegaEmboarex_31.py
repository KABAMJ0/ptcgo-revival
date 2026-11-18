from ptcgo.game.card_effects.attacks_common import recoil_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="549ccdf5-dd4d-56c7-8b89-29d4a5c009de",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaEmboarex.Name",
    display_name="Mega Emboar ex",
    searchable_by=["Mega Emboar ex", "Stage 2", "MEGA", "ex", "MegaEmboarex"],
    subtypes=["Stage 2", "MEGA", "ex"],
    collector_number=31,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=380,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pignite.Name",
    family_id=498,
    abilities=[
        Attack(
            title="Crimson Blast",
            game_text="This Pok\u00e9mon also does 60 damage to itself.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=320,
            effect=recoil_attack(60),
        ),
    ],
)